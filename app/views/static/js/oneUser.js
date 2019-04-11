window.onload = function(){
    let my_url = location.href
    let url = new URL(my_url)
    let user_id = url.searchParams.get('user_id')
    getOneUser(user_id);
}

function getOneUser(person_id){
    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }
    fetch('./api/v2/auth/users/'+person_id, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status === 400){
            document.getElementById('blank').style.display = "block";
            document.getElementById('blank').innerHTML = data.error;
        }
        if (data.status === 401){
            document.getElementById('blank').style.display = "block";
            document.getElementById('blank').innerHTML = data.error;
            window.location.replace('index.html');
        }
        if (data.status === 200){
            console.log(data['data'])
            data.data.forEach((person) => {
                document.getElementById("user_id").innerHTML=`${person.user_id}`;
                document.getElementById("email").innerHTML=`${person.email}`;
                document.getElementById("first_name").innerHTML=`${person.first_name}`;
                document.getElementById("last_name").innerHTML=`${person.last_name}`;
                document.getElementById("phone_number").innerHTML=`${person.phone_number}`;
            })    
        }
    });
    
}