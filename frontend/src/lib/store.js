import { writable } from "svelte/store";
import { readable } from 'svelte/store'
import json from './states.json'

export const state = readable({}, (set) => {
    let index = Math.floor(Math.random() * 10);

    const form = json['states'][index];
	set(form);
	const interval = setInterval(() => {
        let index = Math.floor(Math.random() * 10);

        const form = json['states'][index];
        // console.log(form)
		set(form);
	}, 2000);

	return () => clearInterval(interval);
});

export const focused_elevator = writable(0);
export const current_state = writable();