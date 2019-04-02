document.getElementById('createGroup').addEventListener('submit', createGroup);

function createGroup(event) {
    event.preventDefault();

    token = localStorage.getItem('epicMailToken');

    if (token === null) {
    alert('You must log in');
    window.location.replace('index.html');
    }

    let name = document.getElementById('name').value;

    fetch('https://my-epic-mail.herokuapp.com/api/v2/groups', {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify({"group_name": name})
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status != 200){

            document.getElementById('myStatus').style.display = "block";
            document.getElementById('myStatus').innerHTML = data.error;
            alert(data.error)
        }

        if (data.status === 200){

            document.getElementById('myStatus').style.display = "none";
            alert("Your Group has been successfully created.");

            window.location.replace('groups.html');
        }
    })
    .catch((err) => console.log(err))
}
