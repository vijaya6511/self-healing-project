import datetime

class HealingReporter:

    def __init__(self):
        self.rows = []

    def log(self, element, status, original, healed=None, score=None):
        self.rows.append({
            "element": element,
            "status": status,
            "original": original,
            "healed": healed if healed else "-",
            "score": score if score else "-"
        })

    def generate_report(self, filename="healing_report.html"):
        now = datetime.datetime.now()

        html = f"""
        <html>
        <head>
            <title>Self Healing Report</title>
            <style>
                body {{ font-family: Arial; background:#f4f6f8; padding:20px; }}
                h1 {{ text-align:center; }}
                table {{ border-collapse: collapse; width:100%; background:white; }}
                th, td {{ padding:12px; border:1px solid #ddd; text-align:center; }}
                th {{ background:#2c3e50; color:white; }}
                .PASS {{ background:#2ecc71; color:white; }}
                .HEALED {{ background:#f39c12; color:white; }}
                .FAIL {{ background:#e74c3c; color:white; }}
            </style>
        </head>

        <body>

        <h1>AI Self-Healing Automation Report</h1>
        <p><b>Date:</b> {now}</p>

        <h2>DOM Snapshots</h2>
        <p><a href="original_dom.html" target="_blank">View Original DOM</a></p>
        <p><a href="updated_dom.html" target="_blank">View Updated DOM</a></p>

        <h2>Execution Summary</h2>

        <table>
        <tr>
            <th>Element</th>
            <th>Status</th>
            <th>Original Locator</th>
            <th>Healed Locator</th>
            <th>Score</th>
        </tr>
        """

        for r in self.rows:
            html += f"""
            <tr>
                <td>{r['element']}</td>
                <td class='{r['status']}'>{r['status']}</td>
                <td>{r['original']}</td>
                <td>{r['healed']}</td>
                <td>{r['score']}</td>
            </tr>
            """

        html += """
        </table>
        </body>
        </html>
        """

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)