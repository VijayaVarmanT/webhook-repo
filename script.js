function fetchEvents() {
  fetch('/events')
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('events');
      container.innerHTML = "";

      data.forEach(item => {
        let message = "";
        if (item.type === "push") {
          message = ${item.author} pushed to ${item.to_branch} on ${item.timestamp};
        } else if (item.type === "pull_request") {
          message = ${item.author} submitted a pull request from ${item.from_branch} to ${item.to_branch} on ${item.timestamp};
        } else if (item.type === "merge") {
          message = ${item.author} merged ${item.from_branch} to ${item.to_branch} on ${item.timestamp};
        }
        const p = document.createElement("p");
        p.textContent = message;
        container.appendChild(p);
      });
    })
    .catch(err => console.log(err));
}

setInterval(fetchEvents, 15000);
window.onload = fetchEvents;