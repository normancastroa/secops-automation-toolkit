import json

def main():
    # 1. Get input parameters
    list_name = demisto.args().get('listName', 'AlertName2AlertTypeMapper')
    issue_name_arg = demisto.args().get('issueName', '')

    # 2. Fetch the JSON mapping from the XSOAR List
    list_res = demisto.executeCommand('getList', {'listName': list_name})
    if demisto.isError(list_res):
        return_error(f"Failed to retrieve list '{list_name}': {list_res[0].get('Contents')}")

    list_content = list_res[0].get('Contents')
    try:
        mapping = json.loads(list_content)
    except Exception as e:
        return_error(f"Failed to parse JSON from list '{list_name}': {str(e)}")

    # 3. Determine the list of issue names to process
    if issue_name_arg:
        # argToList handles single values or comma-separated lists automatically
        issue_names = argToList(issue_name_arg)
    else:
        # Fallback to the current incident name from context if issueName is empty
        current_incident = demisto.incident()
        current_name = current_incident.get('name')
        if not current_name:
            return_error("No issueName provided and could not retrieve the current incident name from context.")
        issue_names = [current_name]

    messages = []
    incident_id = demisto.incident().get('id')

    # 4. Match names and assign the corresponding issue type
    for name in issue_names:
        matched_type = None
        for key, issue_type in mapping.items():
            # Supports exact match, prefix match, or containment 
            # (ideal for alert names that append dynamic hostnames)
            if key == name or name.startswith(key) or key in name:
                matched_type = issue_type
                break

        if matched_type:
            set_args = {'type': matched_type}
            if incident_id:
                set_args['id'] = incident_id
                
            res = demisto.executeCommand('setIncident', set_args)
            if demisto.isError(res):
                messages.append(f"Error setting type for '{name}': {res[0].get('Contents')}")
            else:
                messages.append(f"Successfully assigned issue type '{matched_type}' for issue '{name}'.")
        else:
            messages.append(f"No matching mapping found for issue '{name}'.")

    return_results('\n'.join(messages))

if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()