document.getElementById('createGroup').addEventListener('submit', createGroup);

function createGroup(event) {
    event.preventDefault();

    token = localStorage.getItem('token');

    if (token === null) {
    alert('You must log in');
    window.location.replace('index.html');
    }

    let name = document.getElementById('groupName').value;

    fetch('https://my-epic-mail.herokuapp.com/api/v2/groups', {
        method: 'POST',
        cache: 'no-cache',
        headers: {
            'content-type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({"group_name": name})
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status != 201){

            document.getElementById('myStatus').style.display = "block";
            document.getElementById('myStatus').innerHTML = data.error;
            setTimeout(() => { 
                document.getElementById('myStatus').style.display = "none";
            }, 4000);
        }

        if (data.status === 201){

            document.getElementById('myStatus').style.display = "block";
            document.getElementById('myStatus').innerHTML = "Your Group has been successfully created.";

            window.location.replace('groups.html');
        }
    })
    .catch((err) => console.log(err))
}
