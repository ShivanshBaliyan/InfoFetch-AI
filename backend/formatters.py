def format_player(player: dict) -> str:

    batting_stats = {}
    bowling_stats = {}

    for stat in player.get("stats", []):

        if (
            stat["fn"] == "batting"
            and stat["matchtype"] == "odi"
        ):
            batting_stats[stat["stat"].strip()] = stat["value"].strip()

        if (
            stat["fn"] == "bowling"
            and stat["matchtype"] == "odi"
        ):
            bowling_stats[stat["stat"].strip()] = stat["value"].strip()

    return f"""
🏏 Player: {player.get("name", "N/A")}

🌍 Country: {player.get("country", "N/A")}

🎯 Role: {player.get("role", "N/A")}

🏏 Batting Style: {player.get("battingStyle", "N/A")}

📍 Birth Place: {player.get("placeOfBirth", "N/A")}

-------------------------

📊 ODI Batting

Matches : {batting_stats.get("m", "N/A")}
Runs    : {batting_stats.get("runs", "N/A")}
Average : {batting_stats.get("avg", "N/A")}
Strike Rate : {batting_stats.get("sr", "N/A")}
Highest Score : {batting_stats.get("hs", "N/A")}

-------------------------

🎯 ODI Bowling

Wickets : {bowling_stats.get("wkts", "N/A")}
Average : {bowling_stats.get("avg", "N/A")}
Economy : {bowling_stats.get("econ", "N/A")}
Best Bowling : {bowling_stats.get("bbi", "N/A")}
""".strip()


def format_upcoming_matches(matches: dict) -> str:
    data = matches.get("data", [])

    if not data:
        return "No upcoming matches found."

    lines = ["📅 Upcoming Cricket Matches\n"]

    for match in data[:5]:
        lines.append(f"🏏 {match.get('name', 'N/A')}")
        lines.append(f"📍 Venue: {match.get('venue', 'N/A')}")
        lines.append(f"🗓 Date: {match.get('date', 'N/A')}")
        lines.append(f"🏆 Series: {match.get('series', 'N/A')}")
        lines.append("")

    return "\n".join(lines)


def format_match_info(match: dict) -> str:
    lines = [
        f"🏏 {match.get('name', 'N/A')}",
        f"📍 Venue: {match.get('venue', 'N/A')}",
        f"📅 Date: {match.get('date', 'N/A')}",
        f"📊 Status: {match.get('status', 'N/A')}",
        "",
    ]

    scores = match.get("score", [])

    if scores:
        lines.append("Scoreboard:")

        for inning in scores:
            lines.append(
                f"{inning.get('inning')} : "
                f"{inning.get('r')}/{inning.get('w')} "
                f"({inning.get('o')} overs)"
            )

    return "\n".join(lines)


def format_series_list(series: dict) -> str:
    data = series.get("data", [])

    if not data:
        return "No series found."

    lines = ["🏆 Cricket Series\n"]

    for s in data[:5]:
        lines.append(f"🏏 {s.get('name', 'N/A')}")
        lines.append(f"📅 Start: {s.get('startDate', 'N/A')}")
        lines.append(f"📅 End: {s.get('endDate', 'N/A')}")
        lines.append("")

    return "\n".join(lines)


def format_series_info(series: dict) -> str:
    info = series.get("info", {})

    lines = [
        f"🏆 {info.get('name', 'N/A')}",
        f"📅 End Date: {info.get('enddate', 'N/A')}",
        f"🏏 Total Matches: {info.get('matches', 0)}",
        f"🏏 ODI: {info.get('odi', 0)}",
        f"🏏 T20: {info.get('t20', 0)}",
        f"🏏 Test: {info.get('test', 0)}",
        "",
    ]

    matches = series.get("matchList", [])

    if matches:
        lines.append("📋 Matches\n")

        for match in matches:
            lines.append(f"🏏 {match.get('name', 'N/A')}")
            lines.append(f"📅 {match.get('date', 'N/A')}")
            lines.append(f"📍 {match.get('venue', 'N/A')}")
            lines.append(f"📊 {match.get('status', 'N/A')}")
            lines.append("")

    return "\n".join(lines)



