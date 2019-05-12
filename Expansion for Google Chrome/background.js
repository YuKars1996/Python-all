let question = confirm('Будем открывать ссылки?'); #всплывающее окно, подтверждение действия

if (question == true){

let cnt = 0;
    let link = document.getElementsByTagName('a'); #все ссылки на странице
    for(let i = 0; i < link.length; i++){ #пока мы видим все ссылки
#задаем условия для ссылок
        if(link[i].href.indexOf("#адрес, по которому ищем") > -1 && link[i].className == 'pull-right') {
            link[i].innerHTML = '<p>оки</p>'; #если ссылка открыта, вставляем тег р
            window.open(link[i].href); #открываем в новом окне
            cnt++;   
            
        }
    }
if(cnt) {
    alert('Ура, мы все открыли!');
} else {
    console.log('Что-то пошло не так, или нет ссылок');
    alert('А ссылок-то нет...')
}
}   

          
                                

