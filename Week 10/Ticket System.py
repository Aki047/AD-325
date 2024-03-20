import queue
import threading
import random
import time

# Define a Ticket class to represent tickets
class Ticket:
    def __init__(self, ticket_number, timestamp):
        self.ticket_number = ticket_number
        self.timestamp = timestamp

# Function to generate tickets and add them to the queue
def generate_tickets(ticket_queue):
    ticket_number = 1
    while True:
        # Create a new ticket and add it to the queue
        ticket_queue.put(Ticket(ticket_number, time.time()))
        # Print a message indicating that a ticket has been issued
        print("Ticket", ticket_number, "issued.")
        ticket_number += 1
        # Introduce a random delay before generating the next ticket
        time.sleep(random.uniform(2, 30))  # Random interval between 2 to 60 seconds

# Function to process tickets from the queue
def process_tickets(ticket_queue):
    while True:
        # Check if there are tickets in the queue
        if not ticket_queue.empty():
            # Retrieve the next ticket from the queue
            current_ticket = ticket_queue.get()
            # Print a message indicating that the ticket is being processed
            print("Processing ticket number:", current_ticket.ticket_number)
            # Simulate processing time with a random delay
            time.sleep(random.uniform(5, 60))  # Random processing time between 5 to 30 seconds
        else:
            # If there are no more tickets in the queue, print a message and exit the loop
            print("No more tickets to process. Exiting.")
            break

# Main function to orchestrate ticket generation and processing
def main():
    # Create a queue to hold tickets
    ticket_queue = queue.Queue()

    # Create threads for ticket generation and processing
    generate_thread = threading.Thread(target=generate_tickets, args=(ticket_queue,))
    process_thread = threading.Thread(target=process_tickets, args=(ticket_queue,))

    # Start the threads
    generate_thread.start()
    process_thread.start()

    # Wait for the threads to finish executing
    generate_thread.join()
    process_thread.join()

# Entry point of the program
if __name__ == "__main__":
    main()
