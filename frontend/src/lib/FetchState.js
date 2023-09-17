import states from './states.json';


const fetchState = async () => {

    let index = Math.floor(Math.random() * 10);

    const form = states['states'][index];

    await fetch(
        "localhost:8000/prediction",
        {
            headers: {

            },
            method: 'POST',
            body: JSON.stringify(form)
        })
    .then((response) => response.json)
    .then((data) => console.log(data));

}