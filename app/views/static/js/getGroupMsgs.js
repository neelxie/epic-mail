function gropMsgForm() {

    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }

    let reciever = document.getElementById('group_id').value;

    var group_id = parseInt(reciever);

    const URL = './api/v2/groups/'+group_id+'/messages'

    fetch(URL, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
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

            window.location.replace('groups.html');
            alert("Message sent.");
        }
    })
    .catch((err) => console.log(err))
}
