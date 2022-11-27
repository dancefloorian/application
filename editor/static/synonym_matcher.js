let synonyms; //damit du's nachher nöt nomal muessch fetche Jana, wils usserhabl vo de request zugänglich isch

const add_ids = window.setInterval(function(){
  const marks = document.querySelectorAll('mark');
    let counter = 0;
    for (const mark of marks) {
        mark.id = counter.toString();
        counter++;
    }
}, 5000);

const request = new Request(
        "/synonyms",
        {method: 'GET'}
    );
    fetch(request)
        .then((response) => response.json())
        .then((data) => {
            synonyms = data;
            const key_list = Object.keys(data);
            $('textarea').highlightWithinTextarea({
                highlight: key_list
            });
        });