// var updateBtns = document.getElementsByClassName('update-cart')

// for (i = 0; i < updateBtns.length; i++) {
//     updateBtns[i].addEventListener('click', function(){
//         var barangId = this.dataset.barang
//         var action = this.dataset.action
//         console.log('barangId:', barangId, 'action:', action)

//         console.log('USER:', user)
//         if(user === 'AnonymousUser'){
//             console.log('Not logged in')
//         }else{
//             updateUserOrder(barangId, action)       
//         }
//     })
// }

// function updateUserOrder(barangId, action){
//     console.log('User is logged in, sending data..')

//     var url = '/update_item/'

//     fetch(url, {
//         method:'POST',
//         headers: {
//             'Content-Type':'application/json',
//             'X-CSRFToken':csrftoken,
//         },
//         body:JSON.stringify({'barangId': barangId, 'action':action})
//     })
//     .then((response)=>{
//         // if (!response.ok) {
//         //     // error processing
//         //     throw 'Error';
//         // }
//         return response.json()
//         // return response.json()
//     })
//     .then((data)=>{
//         console.log('data:', data)
//         location.reload()

//     })
// } 