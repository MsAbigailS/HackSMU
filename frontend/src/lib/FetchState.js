import states from './states.json';


const fetchState = async () => {

    let index = Math.floor(Math.random() * 10);

    const form = states['states'][index];
    const data = new FormData();
    data.append("outside_temp", String(form.outside_temp));
    data.append("elevator_speed", String(form.elevator_speed));
    data.append("elevator_temp", String(form.elevator_temp));
    data.append("door_speed", String(form.door_speed));
    data.append("usage_time", String(form.usage_time));

    await fetch(
        "http://localhost:5000/predict",
        {
            method: 'POST',
            body: data
        })
    .then((response) => response.text())
    .then((text) => console.log(text))

}

export default fetchState;