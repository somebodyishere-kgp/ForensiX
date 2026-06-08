from utils.file_discovery import discover_files

import config

from reports.excel_reporter import generate_excel_report

from collectors.specialized_collector import (
    collect_metadata
)

from analysers.suspicious import (
    analyze_suspicious
)


def main():

    files = discover_files(
        config.INPUT_DIRECTORY
    )

    results = []

    for file in files:

        print(
            f"Processing {file.name}"
        )

        metadata = collect_metadata(file)
        metadata["suspicious_findings"] = analyze_suspicious(metadata)
        results.append(metadata)

    files = [str(f) for f in files]  # Convert Path objects to strings

    for result in results:

        print()

        for key, value in result.items():

            print(
                f"{key}: {value}"
            )
    
    # Generate Excel report
    generate_excel_report(results, "output/forensix_report.xlsx")
    print("\n✓ Report generated: output/forensix_report.xlsx")

if __name__ == "__main__":
    main()