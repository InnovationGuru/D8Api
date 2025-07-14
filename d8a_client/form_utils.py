"""
Helper functions for working with dynamic form-based pole updates in D8Acapture.

These utilities build valid update payloads using a form's structure,
ensuring that poles appear properly in the web GUI.
"""


def build_pole_update_payload(form, pole_name, lat, lng):
    """
    Build a valid update payload for a pole based on the form structure.

    Args:
        form (dict): Form definition as returned by client.get_form().
        pole_name (str): Name of the pole.
        lat (float): Latitude of the pole.
        lng (float): Longitude of the pole.

    Returns:
        dict: Payload matching the new expected API format with 'fields'.
    """
    fields_payload = {}

    for field in form.get("fields", []):
        field_id = field["id"]
        field_type = field["type"]

        if field_type == "pole_name":
            fields_payload[field_id] = {"value": pole_name}
        elif field_type == "pole_location":
            fields_payload[field_id] = {"value": {"lat": lat, "lng": lng}}
        elif field_type == "nested_form":
            fields_payload[field_id] = {"rows": []}
        elif field_type in {"select", "images", "midspan_photos", "measure_photos"}:
            fields_payload[field_id] = {"value": []}
        elif field_type == "number":
            fields_payload[field_id] = {}  # matches your example with no 'value' key
        else:
            fields_payload[field_id] = {"value": None}

    return {"fields": fields_payload}


def update_pole_with_form(client, pole_id, form, pole_name, lat, lng):
    """
    Shortcut to build and send an update request using a form definition.

    Args:
        client (D8AClient): An instance of the authenticated API client.
        pole_id (str): UUID of the pole to update.
        form (dict): Full form object (from `client.get_form()`).
        pole_name (str): Human-readable pole label.
        lat (float): Latitude coordinate.
        lng (float): Longitude coordinate.

    Returns:
        dict: JSON response from the API.
    """
    payload = build_pole_update_payload(form, pole_name, lat, lng)
    return client.update_pole(pole_id, payload)
