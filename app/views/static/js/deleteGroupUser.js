document.getElementById('deleteUserForm').addEventListener('submit', deleteGroupUser);

function deleteGroupUser(event) {
    event.preventDefault();

    token = localStorage.getItem('token');

    if (token === null) {
    alert('You must log in');
    window.location.replace('index.html');
    }

    let group = document.getElementById('group_id').value;
    let user = document.getElementById('user_id').value;

    let group_id = parseInt(group);
    let user_id = parseInt(user);

    const URL = './api/v2/groups/'+group_id+'/users/'+user_id

    fetch(URL, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.error === "No group by that ID."){

            document.getElementById('myStatus').innerHTML = data.error;
            setTimeout(() => { 
                document.getElementById('myStatus').style.display = "block";
            }, 4000);
        }

        if (data.error === "Can not delete non existant user."){

            document.getElementById('myStatus').innerHTML = data.error;
            setTimeout(() => { 
                document.getElementById('myStatus').style.display = "block";
            }, 4000);
        }

        if (data.status === 200){

            document.getElementById('myStatus').innerHTML = "User has been successfully deleted from Group.";
            setTimeout(() => { 
                document.getElementById('myStatus').style.display = "block";
            }, 4000);

            window.location.replace('groups.html');
        }
    })
    .catch((err) => console.log(err))
}