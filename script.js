function fetchPackets() {
    fetch('http://192.168.12.149:5000/get_packets')
        .then(response => response.json())
        .then(data => {
            let tableBody = document.getElementById("packetTable");
            tableBody.innerHTML = "";
            data.forEach(packet => {
                let row = `<tr>
                    <td>${packet.src}</td>
                    <td>${packet.dst}</td>
                    <td>${packet.protocol}</td>
                </tr>`;
                tableBody.innerHTML += row;
            });
        })
        .catch(error => console.error("Error fetching packets:", error));
}
