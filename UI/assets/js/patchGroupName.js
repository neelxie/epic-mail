document.getElementById('renameGroup').addEventListener('submit', renameGroup);

function renameGroup(event) {
    event.preventDefault();

    token = localStorage.getItem('token');

    if (token === null) {
    alert('You must log in');
    window.location.replace('index.html');
    }

    let groupName = document.getElementById('groupName').value;
    let group = document.getElementById('group_id').value;
    let group_id = parseInt(group);


    fetch('https://my-epic-mail.herokuapp.com/api/v2/groups/'+group_id+'/name', {
        method: 'PATCH',
        cache: 'no-cache',
        headers: {
            'content-type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({"group_name": groupName})
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status != 200){

            document.getElementById('myStatus').innerHTML = data.error;
            setTimeout(() => { 
                document.getElementById('myStatus').style.display = "block";
            }, 4000);
        }

        if (data.status === 200){

            document.getElementById('myStatus').style.display = "none";
            alert("Group name successfully changed.");

            window.location.replace('groups.html');
        }
    })
    .catch((err) => console.log(err))
}