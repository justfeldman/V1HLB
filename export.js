function exportServicesToCSV() {
  const data = [
    ["Service", "Description"],
    ["Accounting Services", "Financial reporting and compliance"],
    ["Business Advisory", "Strategy, growth, and operations optimization"],
    ["Financial Services", "Planning, risk management, investments"],
    ["Tax Services", "Global tax planning, compliance, and advisory"]
  ];

  const csvContent = data.map(row => row.join(",")).join("\n");
  const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = "hlb_services.csv";
  link.style.display = "none";
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
