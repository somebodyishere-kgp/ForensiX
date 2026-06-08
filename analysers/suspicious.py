def analyze_suspicious(metadata):

    findings = []

    check_photoshop(metadata, findings)

    check_gps(metadata, findings)

    check_revision_count(metadata, findings)

    return findings

def check_photoshop(metadata, findings):

    software = str(
        metadata.get("software", "")
    ).lower()

    if "photoshop" in software:

        findings.append(
            {
                "severity": "MEDIUM",
                "finding": "Image Edited",
                "evidence": software
            }
        )

def check_gps(metadata, findings):

    latitude = metadata.get(
        "gps_latitude"
    )

    longitude = metadata.get(
        "gps_longitude"
    )

    if latitude and longitude:

        findings.append(
            {
                "severity": "INFO",
                "finding": "GPS Coordinates Found",
                "evidence": f"{latitude}, {longitude}"
            }
        )

def check_revision_count(
    metadata,
    findings
):

    revisions = metadata.get(
        "revision"
    )

    try:

        revisions = int(revisions)

        if revisions > 100:

            findings.append(
                {
                    "severity": "MEDIUM",
                    "finding": "High Revision Count",
                    "evidence": revisions
                }
            )

    except (ValueError, TypeError):
        pass  # Revision field may not be numeric