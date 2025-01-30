import json

class AgendaHandler:
    FILE_PATH = "agenda.json"

    def __init__(self):
        self.agenda = self.load_agenda()

    def load_agenda(self):
        """Load agenda from a file."""
        try:
            with open(self.FILE_PATH, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_agenda(self):
        """Save agenda to a file."""
        with open(self.FILE_PATH, "w") as file:
            json.dump(self.agenda, file, indent=4)

    def add_meeting(self, title, date, time):
        """Add a meeting to the agenda and save it."""
        meeting = {"title": title, "date": date, "time": time}
        self.agenda.append(meeting)
        self.save_agenda()
        return f"Meeting '{title}' added successfully."

    def remove_meeting(self, title):
        """Remove a meeting by title and save changes."""
        for meeting in self.agenda:
            if meeting["title"] == title:
                self.agenda.remove(meeting)
                self.save_agenda()
                return f"Meeting '{title}' removed successfully."
        return f"Meeting '{title}' not found."

    def view_meeting_list(self):
        """Return a formatted string of meetings."""
        if not self.agenda:
            return "No meetings in the agenda."

        output = "\n### Meeting List:\n"
        output += "| # | Title           | Date       | Time   |\n"
        output += "|---|-----------------|------------|--------|\n"
        for i, meeting in enumerate(self.agenda, 1):
            output += f"| {i} | {meeting['title']:<15} | {meeting['date']} | {meeting['time']} |\n"
        return output

    def view_complete_agenda(self):
        """Return a formatted string of meetings grouped by date."""
        if not self.agenda:
            return "No meetings in the agenda."

        agenda_by_date = {}
        for meeting in self.agenda:
            date = meeting["date"]
            if date not in agenda_by_date:
                agenda_by_date[date] = []
            agenda_by_date[date].append(meeting)

        output = "\n### Complete Agenda by Date:\n"
        for date, meetings in sorted(agenda_by_date.items()):
            output += f"\nDate: {date}\n"
            output += "| # | Title           | Time   |\n"
            output += "|---|-----------------|--------|\n"
            for i, meeting in enumerate(meetings, 1):
                output += f"| {i} | {meeting['title']:<15} | {meeting['time']} |\n"

        return output
