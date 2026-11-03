
import csv
import os


class Task:

    def __init__(self, sub, topic, date, hrs):
        self.sub = sub
        self.topic = topic
        self.date = date
        self.hrs = hrs
        self.done = False

    def show(self):
        status = "Done" if self.done else "Pending"

        print("\nSubject:", self.sub)
        print("Topic:", self.topic)
        print("Date:", self.date)
        print("Duration:", self.hrs, "hours")
        print("Status:", status)


class Planner:

    def __init__(self):
        self.tasks = []
        self.file = "study_tasks.csv"
        self.load()

    def add(self):
        print("\n--- Add Study Task ---")

        sub = input("Enter subject: ")
        topic = input("Enter topic: ")

        date = input("Enter date (DD-MM-YYYY): ")

        while True:
            try:
                hrs = float(input("Enter study hours: "))

                if hrs > 0:
                    break

                print("Hours must be greater than 0.")

            except ValueError:
                print("Enter a valid number.")

        t = Task(sub, topic, date, hrs)
        self.tasks.append(t)
        self.save()

        print("\nTask added successfully!")

    def view(self):
        print("\n--- Your Study Tasks ---")

        if not self.tasks:
            print("No tasks added yet.")
            return

        for i, t in enumerate(self.tasks, 1):
            print("\nTask", i)
            t.show()

    def complete(self):
        self.view()

        if not self.tasks:
            return

        try:
            n = int(input("\nEnter task number to complete: "))

            if 1 <= n <= len(self.tasks):
                self.tasks[n - 1].done = True
                self.save()
                print("Task completed!")

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a number.")

    def delete(self):
        self.view()

        if not self.tasks:
            return

        try:
            n = int(input("\nEnter task number to delete: "))

            if 1 <= n <= len(self.tasks):
                self.tasks.pop(n - 1)
                self.save()
                print("Task deleted!")

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a number.")

    def progress(self):
        total = len(self.tasks)
        done = sum(t.done for t in self.tasks)
        pending = total - done

        print("\n--- Study Progress ---")
        print("Total tasks:", total)
        print("Completed:", done)
        print("Pending:", pending)

        if total > 0:
            per = (done / total) * 100
            print("Progress:", round(per, 2), "%")
        else:
            print("No tasks to track yet.")

    def save(self):
        with open(self.file, "w", newline="") as f:
            w = csv.writer(f)

            w.writerow(["Subject", "Topic", "Date", "Hours", "Done"])

            for t in self.tasks:
                w.writerow([
                    t.sub,
                    t.topic,
                    t.date,
                    t.hrs,
                    t.done
                ])

    def load(self):
        if os.path.exists(self.file):
            with open(self.file, "r", newline="") as f:
                r = csv.DictReader(f)

                for row in r:
                    t = Task(
                        row["Subject"],
                        row["Topic"],
                        row["Date"],
                        float(row["Hours"])
                    )

                    t.done = row["Done"] == "True"
                    self.tasks.append(t)

    def menu(self):
        while True:
            print("\n========================")
            print("     STUDY PLANNER")
            print("========================")
            print("1. Add task")
            print("2. View tasks")
            print("3. Complete task")
            print("4. Delete task")
            print("5. View progress")
            print("6. Exit")
            print("========================")

            ch = input("Enter your choice: ")

            if ch == "1":
                self.add()

            elif ch == "2":
                self.view()

            elif ch == "3":
                self.complete()

            elif ch == "4":
                self.delete()

            elif ch == "5":
                self.progress()

            elif ch == "6":
                print("\nBye! Happy studying!")
                break

            else:
                print("Invalid choice. Try again.")


p = Planner()
p.menu()
