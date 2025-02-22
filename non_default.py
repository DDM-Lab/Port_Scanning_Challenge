#!/usr/bin/env python3
import random


def simulate_port_scan(ports):
    """
    Simulate a port scan by returning all ports as open.
    """
    return sorted(ports)


def format_nmap_output(open_ports, scanned_ports):
    """
    Formats and displays output similar to an Nmap scan.
    Every port in the scanned list is shown with its state
    (which will be "open" for all ports in this version) and its corresponding service.
    """
    print("\nNmap scan report:")
    print(f"Ports scanned: {len(scanned_ports)}")
    print("Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-29 02:00 EST\n")
    print("PORT     STATE   SERVICE")
    services = {
        8081: "http-alt",
        8443: "https-alt",
        9000: "cslistener",
        9001: "tor-orport",
        10000: "webmin",
        12345: "netbus",
    }
    for port in scanned_ports:
        state = "open" if port in open_ports else "closed"
        service = services.get(port, "unknown")
        print(f"{port:<8} {state:<7} {service}")
    print("\nNmap done: 1 IP address (1 host up) scanned")


def connect_to_port(port, encoded_parts, connected_ports):
    """
    Connects to a specified port and reveals an encoded part if available.
    If the port hasn't been connected before and an encoded part exists,
    the part is popped from the list and displayed.
    """
    if port not in connected_ports and encoded_parts:
        connected_ports.append(port)
        encoded_part = encoded_parts.pop(0)
        part_number = len(connected_ports)
        print(f"\nConnected to port {port}")
        print(f"Encoded part {part_number} of 4 found: {encoded_part}")
        
        if part_number == 1:
            print("\nMilestone: You found the first encoded part!")
        elif part_number == 4:
            print("\nMilestone: You found all encoded parts!")
            return True
    elif port in connected_ports:
        print(f"\nAlready connected to port {port}. No new encoded parts.")
    else:
        print(f"\nConnected to port {port}, but no new encoded parts found.")
    
    return False


def analyze_text(encoded_text):
    """
    Simulates analyzing the complete encoded text.
    """
    print("\nNow it's time to analyze the encoded text and find the flag!")
    print(f"Encoded text: {encoded_text}")


def main():
    """
    Main function to run the Port Scanner Challenge game.
    """
    # Pre-defined encoded text (for demonstration purposes)
    encoded_text = "iVBORw0KGgoAAAANSUhEUgAAArcAAADpCAYAAAA+hh/ZAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAACoFSURBVHhe7d15eBRVov7xtzuLJMCQQADZArJIJCq5yuqwKaOoRGZGYbziCC7MoLggwgOIOjoKCAg6wohcBxRk7qiAA7INiugYwGFTQIyEHQSSAAEDWcAk9Pn9cdP16650dzoQJBbfz/PUP31OdU6qa3nrVNUplzHGCAAAAHAAt/0DAAAA4OeKcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzC7QWwZMkSuVwuNW3aVFlZWfbii+rgwYN69tln1bJlS7lcLmtq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SVGdOnXsVcJ25swZHTt2TCrn9qK4uDjrxDLU9hWO5ORkRUZG6vTp09q5c6dfWdu2bfX++++rY8eO59WTeD7beUZGhg4fPixJuummm86rHV6HDh3SsWPHZIxRv379NGnSJOt2FO9IG927d/9JR0epim262Fq2bKlJkyZJkjZu3Ki33nrrkgn3FwrhNgzNmzdXWlqabr75ZkVERKhWrVoaPXq0Xn75ZUnS22+/HdaQMUuXLtXKlSvldrv13nvv6bHHHlOtWrXkcrl07bXXauHChWrevLlycnKsJx4/+ugjLV26VCp9svhPf/qTdVCpX7++pk6dao25N2vWLP373/+2/p73Ml7t2rXVoEED6/Ofs/z8fOs+0HDu1XK5XHr88ceVnJwsY4zGjBkT1uXNkpISqyc81KXBatWqKSEhQfK5FziQc23HuYqMjLTuhTx69KjOnDljr2IZOHCgoqOj1aVLF33++edq0KCBVq1apT59+tirVopPP/1U06ZNU/PmzfX888+HXL4IbOLEiYqMjNS1116r999/X9HR0frHP/5h3QMeSsuWLfWnP/1JKh2+avr06WEdSE+cOGGdJCUnJ59X+CouLrbGLw31+1erVk316tWTytm+whETE6Po6GipNGBdCOeznW/fvl2SFBsbW+H7fYPZuXOndetc8+bNtWLFChUVFVkjvnhvVZsxY4Zee+21sNaD81UV21QV3HXXXUpNTZVKR93YsGGDvUpI8fHxioyM1L59+5SXl2cvvuQQbsMwbNiwMpeIXKUDPCclJamoqEgff/yxX7md7yW9YPe/NmvWTP3791fdunV14sQJFRYWWvP06tVLd999d5kDim87PB6P34DZ3h6ZiIgIRURE+Mx18fXp00euAINm+06BBv8+duyYdu/erejoaOsBjvLUq1dPr732mtxu9zmNKdiqVSv7RxbfEFme821HRTVu3Nj+URm+PdReWVlZeuSRR0KesH3xxReqWbNmmd/Mdwo0APuhQ4f0xBNPSKWXxe3bFcLj7eHzKioq0tChQ7Vs2bKwwsDAgQOtA+mkSZO0ZcsWe5UyCgsLrZOkytyfhNq+oqKiwt6+yhMfH69f/OIX9o8r3blu597wXq1aNcXGxtqLz0l2drbq1q2rpKQkrVq1Sr169VJUVJRcLpfatGmjRYsW6f7775ckvfzyy+UOaVgZLnabCgsL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lJKSEvCE51JBuC1HdnZ20Idqjh49qq+//loqDUKhNsA6derov/7rv6TS104GC5rr1q1TQUGBIiIidPnll1sH9MWLFwe9j+7IkSNauXKlZOulq1WrlnXPzSeffKLFixf7zRfInj17NHfuXKl0rMVzGcz8QmrWrJnatm0b8jWj5bGPKfiXv/zFXkUqDavR0dHauXNn0B7srVu36sSJE+UOnh9IuO2oqJMnT2r69OlSae/9jTfeaJV5e0O3bdsWNJyUlJRYIyU0b97c6k06H3fccYeMMUGnzMxMK7xMmDBBxhgdOHDA6t2TT8+WMUaLFi0KeYlXpa97PX36tGJjYyv08GFVU7duXZ06dUqZmZlatWqVvdiyfv16qfQB0+bNm9uLg3K5XHryySetA+lzzz0XNETfdNNN1jBX48ePD7pP8jLG6N1339WxY8fkdrvVv39/64B7ww03SJK+/vrroD3Na9askTHmvF8osmLFCms//vvf//6CjN8cTLjbeWRkpIYMGaLo6Gjt3r1bL730UshbNsoTHx9v9bSvWrUq6G+1adMmbd++XS6XK+AoPpWpKrYpXNWrV7deQvLll1+We/zZv3+/9brpDh06VPgEu06dOpoyZYr1UpBnn3025AOR3peTNGnSRG3btrUXX3IIt2GYPn16mY3QGKM5c+YoIyNDCQkJ1rA6wURGRlpvBlq5cmXAp2f3799v9Zr07dtXcXFx1jzr16/XwoULyxzQfdvhdrt19913+5Xfc8896tmzp4wxevjhh/Xll1/6lfvKzs7Wgw8+qKysLEVHR2vkyJEV6gH6KfiOKxuqB7w8vmMKBnuzWEpKim688UaVlJRo6tSpZQ40x48f16uvvipJuvXWW9WkSRO/8nCE046KOH36tIYPH2696Wjo0KF+l8Ouu+46JSUlyRijN954I+BJ1kcffaR58+ZJpeuh7ytTLybfnq0333wz5KgAGzZs0Ouvvy5J6tq1a5U7SauIK6+80gqCM2bMCHhLhu//27t37wr3ctapU0fjxo2T2+0OedtHvXr19Oc//1lut1urV6/W8OHDA65D8tk3jR8/Xipd172/n0pHFEhKSlJ2drbeeeedMvu23bt366233pJK36x2roH0yy+/1MMPPyxjjJKTk/W73/3OXuWCC3c779Kli/Xa37/97W8aNWpU0OXrdejQIb344otlHkKr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ljcs6aWCcIufHe8A7J9//nnQIYsAALgUZGZmWuM4t27dOuSwpJcKwi1+drp3766kpCTt3btXbdq0UfXq1fXVV1/ZqwEA4FhZWVlq2rSpGjVqpDVr1ighIUH9+/e3V7skEW7xs9O4cWN99NFH6tq1q70IqFLy8/PVo0cPuWyvGw536tGjR9C34wGVrSqur1WxTVVR+/bttWjRIr8H1S9lPFAGABdIQUGBHnrooZAvTwnlhhtu0KxZsyrliWugPFVxfa2KbULVR7gFAACAY3BbAgAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAAByDcAsAAADHINwCAADAMQi3AAAAcAzCLQAAABzj/wHJaHGr39vKtgAAAABJRU5ErkJggg=="
    
    # Split the encoded text into roughly equal parts
    part_length = len(encoded_text) // 4
    encoded_parts = [
        encoded_text[i:i + part_length] for i in range(0, len(encoded_text), part_length)
    ]
    
    connected_ports = []
    
    # List of non-default ports available for scanning
    ports_to_scan = [8081, 8443, 9000, 9001, 10000, 12345]
    
    open_ports = []  # This will be updated via simulate_port_scan
    attempted_ports = set()

    print("Welcome to the Port Scanner Challenge!")
    print("Scan ports to find open ones, then connect to reveal encoded parts.")
    print("Commands: 'scan', 'connect <port>', or 'exit'")
    
    while True:
        user_input = input("\nEnter command: ").lower().split()
        
        if not user_input:
            continue

        command = user_input[0]
        
        if command == "exit":
            break
        elif command == "scan":
            open_ports = simulate_port_scan(ports_to_scan)
            format_nmap_output(open_ports, ports_to_scan)
        elif command == "connect" and len(user_input) == 2:
            try:
                port = int(user_input[1])
                attempted_ports.add(port)
                if port in open_ports:
                    all_parts_found = connect_to_port(port, encoded_parts, connected_ports)
                    if all_parts_found:  # All parts have been revealed
                        analyze_text(encoded_text)
                        break
                else:
                    print(f"\nPort {port} is not open or hasn't been scanned yet.")
            except ValueError:
                print("Invalid port number. Please enter a valid number.")
        else:
            print("Invalid command. Use 'scan', 'connect <port>', or 'exit'.")

    # Summary of results after exiting or completing the challenge
    print("\nChallenge complete. Thanks for participating!")
    print(f"\nPorts connected: {connected_ports}")
    print("Please copy the order of the ports.")
    print(f"Total unique ports connected: {len(connected_ports)}")
    print(f"Total ports attempted: {len(attempted_ports)}")
    
    invalid_attempts = len(attempted_ports - set(ports_to_scan))
    
    print(f"Invalid ports attempted: {invalid_attempts}")


if __name__ == "__main__":
    main()
