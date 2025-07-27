from ticket import Customer
from utils import waiting_list, customer_records, available_tickets, currently_serving,  log_to_file, init_db, save_to_db, view_logs, view_db_records
from datetime import datetime

def assign_customer():
    name = input("Enter customer's name: ").strip()
    reason = input("Enter reason for visit: ").strip()

    if not available_tickets:
        print("No tickets available now.")
        return

    # Assign the lowest available ticket number
    ticket_no = min(available_tickets)
    available_tickets.remove(ticket_no)

    customer = Customer(name, reason)
    customer_records[ticket_no] = customer
    waiting_list.put(ticket_no)

    log_to_file(f"Customer {name} assigned Ticket #{ticket_no} for reason: {reason}")
    save_to_db(ticket_no, name, reason, customer.timestamp.strftime('%Y-%m-%d %H:%M:%S'))

    print(f"Ticket assigned: {ticket_no}. Please wait to be called.")

def serve_next_customer():
    global currently_serving

    if waiting_list.empty():
        print("No customers in queue.")
        return

    ticket_no = waiting_list.get()
    currently_serving = ticket_no
    customer = customer_records[ticket_no]

    print(f"\n🔔 Now serving Ticket #{ticket_no}")
    print(f"Name  : {customer.name}")
    print(f"Reason: {customer.reason}")
    customer.add_history("Served")
    customer.display_history()

    log_to_file(f"Ticket #{ticket_no} ({customer.name}) has been served.")
    save_to_db(ticket_no, customer.name, customer.reason, customer.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
               datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Display customer history
def show_customer_history():
    try:
        ticket_no = int(input("Enter ticket number: ").strip())
        customer = customer_records.get(ticket_no)
        if customer:
            customer.display_history()
        else:
            print("No customer found with that ticket number.")
    except ValueError:
        print("Invalid input. Enter a valid number.")

def main():
    init_db()
    while True:
        print("\n--- Bank Queue System ---")
        print("1. Add new customer")
        print("2. Serve next customer")
        print("3. View customer history")
        print("4. View activity log")
        print("5. View all customer records")
        print("6. Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':
            assign_customer()
        elif choice == '2':
            serve_next_customer()
        elif choice == '3':
            show_customer_history()
        elif choice == '4':
            view_logs()
        elif choice == '5':
            view_db_records()
        elif choice == '6':
            print("Exiting system. Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
