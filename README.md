Important Notes
Ethical Usage: Ensure you have permission to scan the target before using this tool. Unauthorized scanning may violate laws or policies. Always adhere to ethical guidelines.
Limitations: This script scans for open TCP ports. It does not check for UDP ports or perform service enumeration.

This Python script is a comprehensive port scanning tool designed to identify open ports on a given target IP address. It offers a simple, interactive interface for users to specify their scanning preferences and combines efficiency with flexibility. This tool provides valuable insights into network services.

Features:

Interactive Target Input:
Prompts users to input the target IP address or hostname for scanning.

Custom Port Range Selection:
Users can specify the range of ports to scan, allowing flexibility based on their needs (e.g., scanning only commonly used ports or the entire range).

Multithreaded Scanning:
The script leverages multithreading to scan multiple ports simultaneously, significantly improving scanning speed compared to sequential approaches.

Error Handling:
Validates user input to ensure proper port range and target IP address format.
Catches and handles common errors like unreachable hosts or invalid ports.

Real-Time Feedback:
Displays open ports as they are discovered, providing a dynamic and engaging scanning experience.

Cross-Platform Compatibility:
Built entirely with Python, the script runs seamlessly on Windows, macOS, and Linux.
