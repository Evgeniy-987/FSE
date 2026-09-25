import sys


def compute_wind_chill(air_temp_f: float, wind_speed_mph: float):
    if wind_speed_mph > 3:
        wc_temp = (35.74 + 0.6125 * air_temp_f +
                   (0.4275 * air_temp_f - 35.75) * wind_speed_mph ** 0.16)
    else:
        wc_temp = float(air_temp_f)
    wc_effect = wc_temp - air_temp_f
    return wc_temp, wc_effect


def process_file(input_path: str, output_path: str) -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # line 0 -> header, line 1 -> separator, line 2+ -> data
    data_lines = lines[2:]

    results = []
    for raw_line in data_lines:
        line = raw_line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 3:
            continue
        time_str, air_temp_str, wind_speed_str = parts[0], parts[1], parts[2]
        air_temp = float(air_temp_str)
        wind_speed = float(wind_speed_str)
        wc_temp, wc_effect = compute_wind_chill(air_temp, wind_speed)
        results.append((time_str, wc_temp, wc_effect))

    avg_temp = sum(r[1] for r in results) / len(results) if results else 0.0

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"{'Time':<12}{'WC temp':<12}{'WC Effect':<12}\n")
        f.write("-" * 30 + "\n")
        for time_str, wc_temp, wc_effect in results:
            f.write(f"{time_str:<12}{wc_temp:<12.1f}{wc_effect:<12.1f}\n")
        f.write("-" * 30 + "\n\n")
        f.write(
            f"The average adjusted temperature, based on {len(results)} "
            f"observations, was {avg_temp:.1f}\n"
        )


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python wind_chill.py <X>")
        print("Reads X.WCData.txt and writes X.WindChillReport.txt")
        sys.exit(1)

    prefix = sys.argv[1]
    input_path = f"{prefix}.WCData.txt"
    output_path = f"{prefix}.WindChillReport.txt"
    process_file(input_path, output_path)
    print(f"Report written to {output_path}")


if __name__ == "__main__":
    main()