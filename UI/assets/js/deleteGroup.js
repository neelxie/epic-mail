function deleteGroup(group_id){
    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }
    fetch('https://my-epic-mail.herokuapp.com/api/v2/groups/'+group_id, {
        method: 'DELETE',
        headers: {

            'Authorization': `Bearer ${token}`
        }
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status === 404){

            document.getElementById('blank').innerHTML = "Can not delete a non existant group.";
            setTimeout(() => { 
                document.getElementById('blank').style.display = "block";
            }, 4000);
            window.location.replace('groups.html');
        }
        if (data.status === 200){
            alert("Group successfully deleted.")
            document.getElementById('blank').innerHTML = "Group successfully deleted.";
            setTimeout(() => { 
                document.getElementById('blank').style.display = "block";
            }, 4000);
            window.location.replace('groups.html');
        }
    })
    .catch((err) => console.log(err))
}