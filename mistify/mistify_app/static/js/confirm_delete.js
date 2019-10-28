var deleteButtons = document.querySelectorAll('.delete');

deleteButtons.forEach(function(button){
  button.addEventListener('click',function(ev){
    var confirmDel = confirm("Delete result - are you sure?");

    if (!confirmDel){
      ev.preventDefault();
    }
  })
});
