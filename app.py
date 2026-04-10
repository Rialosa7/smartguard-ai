def generate_tasks(goal):
    goal = goal.lower()

    if "trading" in goal:
        return [
            "Learn basic trading concepts",
            "Open a demo trading account",
            "Practice reading charts",
            "Start small real trades"
        ]
    else:
        return ["Break your goal into smaller actionable steps"]


def check_scam(url):
    suspicious_keywords = ["free", "fast", "win", "bonus"]

    for word in suspicious_keywords:
        if word in url.lower():
            return "⚠️ Potential Scam Detected"

    return "✅ Looks Safe"


def main():
    print("=== SmartGuard AI ===")
    print("1. Generate Tasks")
    print("2. Check Scam URL")

    choice = input("Choose (1/2): ")

    if choice == "1":
        goal = input("Enter your goal: ")
        tasks = generate_tasks(goal)

        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

    elif choice == "2":
        url = input("Enter URL: ")
        print(check_scam(url))


if __name__ == "__main__":
    main()