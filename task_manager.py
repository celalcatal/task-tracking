import json
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("❌ Hatalı JSON formatı. Yeni dosya oluşturuluyor.")
        return []

def save_tasks(tasks):
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"❌ Dosya kaydedilemedi: {e}")

def valid_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_task():
    title = input("Görev Başlığı: ").strip()
    if not title:
        print("⚠️ Başlık boş olamaz.")
        return

    description = input("Açıklama: ").strip()
    assignee = input("Atanan Kişi: ").strip()
    due_date = input("Son Tarih (YYYY-MM-DD): ").strip()

    if not valid_date(due_date):
        print("❌ Geçersiz tarih formatı. (Doğru format: YYYY-MM-DD)")
        return

    task = {
        "title": title,
        "description": description,
        "assignee": assignee,
        "due_date": due_date,
        "status": "Not Started"
    }

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Görev eklendi.")

def list_tasks(filter_by=None, filter_value=None):
    tasks = load_tasks()
    if not tasks:
        print("📭 Görev bulunamadı.")
        return
    for idx, task in enumerate(tasks):
        if filter_by and task.get(filter_by) != filter_value:
            continue
        print(f"\n[{idx}] {task['title']} ({task['status']})")
        print(f"   Açıklama: {task['description']}")
        print(f"   Atanan: {task['assignee']}")
        print(f"   Son Tarih: {task['due_date']}")

def update_task_status():
    tasks = load_tasks()
    if not tasks:
        print("📭 Güncellenecek görev yok.")
        return
    list_tasks()
    try:
        index = int(input("\nDurumu güncellenecek görevin numarası: "))
        if index < 0 or index >= len(tasks):
            print("❌ Geçersiz görev numarası.")
            return
    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin.")
        return

    new_status = input("Yeni Durum (Not Started/In Progress/Completed): ").strip()
    if new_status not in ["Not Started", "In Progress", "Completed"]:
        print("❌ Geçersiz durum değeri.")
        return

    tasks[index]["status"] = new_status
    save_tasks(tasks)
    print("✅ Durum güncellendi.")

def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("📭 Silinecek görev yok.")
        return
    list_tasks()
    try:
        index = int(input("\nSilinecek görevin numarası: "))
        if index < 0 or index >= len(tasks):
            print("❌ Geçersiz görev numarası.")
            return
    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin.")
        return

    deleted = tasks.pop(index)
    save_tasks(tasks)
    print(f"🗑️ '{deleted['title']}' silindi.")

def main():
    while True:
        print("\n--- Görev Takip Sistemi ---")
        print("1. Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Durum Güncelle")
        print("4. Görev Sil")
        print("5. Filtrele (Atanan)")
        print("6. Çıkış")

        choice = input("Seçiminiz: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            update_task_status()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            name = input("Atanan kişinin adı: ").strip()
            list_tasks("assignee", name)
        elif choice == "6":
            print("👋 Çıkılıyor...")
            break
        else:
            print("❌ Geçersiz seçim.")

if __name__ == "__main__":
    main()
