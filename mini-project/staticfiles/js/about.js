function openNav() {
    document.getElementById("mobile-menu").style.height = "100%";
}

function closeNav() {
    document.getElementById("mobile-menu").style.height = "0";
}

// $(document).ready(function () {
//     $('#data-form-1').submit(function (event) {
//         event.preventDefault();
//         $.ajax({
//             type: 'POST',
//             url: '/email_submit/',
//             data: $(this).serialize(),
//             success: function (response) {
//                 if (response.success) {
//                     $('#message').html('<p>Data was successfully saved.</p>');
//                 } else if (response.error) {
//                     $('#message').html('<p>Error: ' + response.error + '</p>');
//                 } else {
//                     $('#message').html('<p>Unknown error</p>');
//                 }
//             },
//             error: function (xhr, textStatus, error) {
//                 console.log('Error:', error);
//                 console.log('Status:', xhr.status);
//                 console.log('Status Text:', xhr.statusText);
//                 console.log('Response Text:', xhr.responseText);
//                 $('#message').html('<p>Error: ' + error + '</p>');
//             }
//         });
//     });

//     $('#data-form-2').submit(function (event) {
//         event.preventDefault();
//         $.ajax({
//             type: 'POST',
//             url: '/email_submit/',
//             data: $(this).serialize(),
//             success: function (response) {
//                 if (response.success) {
//                     $('#message').html('<p>Data was successfully saved.</p>');
//                 } else if (response.error) {
//                     $('#message').html('<p>Error: ' + response.error + '</p>');
//                 } else {
//                     $('#message').html('<p>Unknown error</p>');
//                 }
//             },
//             error: function (xhr, textStatus, error) {
//                 console.log('Error:', error);
//                 console.log('Status:', xhr.status);
//                 console.log('Status Text:', xhr.statusText);
//                 console.log('Response Text:', xhr.responseText);
//                 $('#message').html('<p>Error: ' + error + '</p>');
//             }
//         });
//     });
// });
