# Network Security Anomalies Dashboard App

A web-based educational tool for simulating and visualizing common network security attacks through packet-level forensic analysis.

![Network Security Visualization](https://img.shields.io/badge/Network-Security%20Visualization-blue)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Forensics-red)
![Educational Tool](https://img.shields.io/badge/Educational-Tool-green)

## Overview

This tool provides an interactive visualization of common network attacks at both Layer 2 (Data Link) and Layer 3 (Network) of the OSI model. It demonstrates how network security forensics can detect patterns indicative of various attacks by analyzing packet headers and traffic flows.

## Features

- **Interactive Attack Selection**: Choose from 10 common network attacks across Layer 2 and Layer 3
- **Real-time Packet Visualization**: See packet details as they would appear in a packet capture
- **Attack Pattern Recognition**: Observe how attack patterns develop over time
- **Threshold-based Detection**: Watch as detection thresholds are triggered based on packet patterns
- **Educational Information**: Learn about each attack's characteristics, detection patterns, and mitigation strategies
- **Forensic Analysis Demonstrations**: Understand the packet-level indicators used to detect attacks

## Attacks Covered

### Layer 3 (Network) Attacks
- Port Scanning
- DDoS (Distributed Denial of Service)
- IP Spoofing
- SYN Flooding
- ICMP Flooding
- Lateral Movement (New)

### Layer 2 (Data Link) Attacks
- MAC Flooding
- ARP Spoofing/Poisoning
- VLAN Hopping
- MAC Spoofing
- DHCP Starvation

## Usage

1. Select an attack type from either Layer 2 or Layer 3 categories
2. Click "Simulate Attack" to see the packet flow visualization
3. Observe the metrics panel to track packet count, anomaly score, and elapsed time
4. Watch for the detection alert when suspicious patterns exceed thresholds
5. Review detailed information about the attack pattern and mitigation strategies
6. Use the "GenAI Log Analyzer" button for deeper analysis with AI assistance

## Technical Details

This tool simulates packet-level details that would typically be observed in tools like Wireshark. For each attack, it demonstrates:

- Source and destination IP addresses
- Source and destination ports
- Protocol information
- TCP/UDP flags
- Packet size and TTL values
- MAC addresses (for Layer 2 attacks)
- VLAN tags (for certain Layer 2 attacks)
- Trusted vs untrusted sources (for lateral movement detection)

The detection methodology demonstrates how security systems establish baselines and thresholds to identify anomalous behavior, correlating packet characteristics over time to recognize attack signatures.

## Deployment

### Local Deployment

To run this tool locally:

1. Clone this repository
2. Open `Network-Security-Anomalies.html` in any modern web browser

No additional dependencies or setup required!

### Server Deployment

This tool is a single-page HTML application with vanilla JavaScript, making it extremely portable and easy to deploy on any web server or hosting platform.

## Deployment Options

### GitHub Pages (Recommended for Static Content)

1. Push the repository to GitHub
2. Enable GitHub Pages in the repository settings
3. Select the branch containing your HTML file

GitHub Pages works well for this project because:
- It's free and designed for static content
- Provides HTTPS by default
- Easy to update with new git pushes
- No server-side processing needed

### Render

Render is also a good option for deploying static sites:
1. Connect your GitHub repository
2. Select "Static Site" deployment type
3. Configure the build command (not needed for this project)
4. Set the publish directory to the one containing your HTML file

### Streamlit Deployment

Since this is a pure HTML/JS application, Streamlit isn't the ideal deployment platform as it's primarily designed for Python-based web apps. If you want to use Streamlit, you would need to:

1. Create a Python wrapper that serves the HTML content
2. Use Streamlit's components to display the HTML

Example `app.py` for Streamlit:

```python
import streamlit as st
import streamlit.components.v1 as components

st.title("Network Security Attack Visualizer")

# Read the HTML file
with open("Network-Security-Anomalies.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Display the HTML content
components.html(html_content, height=800)
```

## Future Enhancements

- Adding packet capture (PCAP) file import functionality
- Implementing actual network traffic scanning
- Adding more attack types and detection methods
- Creating an API interface for integration with security monitoring tools

## Deployment Instructions

### Local Development

1. Set up a Python environment:
```bash
conda create -p venv python=3.12 -y
conda activate venv
pip install -r requirements.txt
```

2. Run the application locally:
```bash
# For simple HTML viewing:
python -m http.server
# Then open http://localhost:8000/Network-Security-Anomalies.html
```

### GitHub Pages Deployment

1. Clone the repository:
```bash
git clone https://github.com/lhiebert01/network-security-anomalies-dashboard-app.git
cd network-security-anomalies-dashboard-app
```

2. Make your changes and push to GitHub:
```bash
git add .
git commit -m "Your commit message"
git push origin main
```

3. Enable GitHub Pages in the repository settings.

4. Your visualization will be available at `https://lhiebert01.github.io/network-security-anomalies-dashboard-app/`

## Integration with GenAI Network Analyzer

This visualization tool integrates with a GenAI-powered Network Log Analyzer that provides:

- AI-assisted analysis of network traffic patterns
- Natural language explanations of detected attacks
- Recommendations for mitigation strategies
- Deeper insights into complex attack patterns

Access the GenAI Network Analyzer directly from the dashboard via the purple "GenAI Log Analyzer" button.

## Requirements

- Modern web browser with JavaScript enabled
- No additional dependencies required

## License

For educational purposes only. Do not use for malicious activities.

## Author

Created by [Lindsay Hiebert](https://www.linkedin.com/in/lindsayhiebert/)

## Acknowledgements

- Network security community
- Packet analysis and forensics experts
- Cybersecurity education resources