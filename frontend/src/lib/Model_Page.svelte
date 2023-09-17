<script lang='ts'>
	import Canvas from "./Canvas.svelte";
    import fetchState from './FetchState';
    import { focused_elevator } from "$lib/store";    
    import { current_state, state } from '$lib/store';

    state.subscribe((state) => fetchState(state));
    // console.log(state);
    let current_elevator = 0;
    let popup: HTMLDivElement | null = null;
    let thing : {
        [key : string]: string
    } = $state 

    focused_elevator.subscribe(value => {
        if (popup == null) return;
        if (value == 0) {
            popup.style.opacity = '0';
        } else {
            current_elevator = $focused_elevator;
            popup.style.opacity = '1';
        }

    })

    function updateElevatorValue() {
        current_elevator = $focused_elevator;
    }

</script>

<main>

    <div class="fill">
        <Canvas/>
    </div>

    <div id="popup" data-theme="light" bind:this={popup} on:transitionend={() => {updateElevatorValue()}}>
        <hgroup>
            <h3>{#if current_elevator < 5}Elevator {current_elevator}{:else}HVAC {current_elevator % 4}{/if}</h3>
            <h3>Condition: Good</h3>
        </hgroup>

        Current State is: {$current_state}
        <br/>
        {#if current_elevator < 5}Current Elevator Temperature is: {thing['outside_temp']}{/if}
        <br/>
        {#if current_elevator < 5}Current Elevator Door Speed is: {thing['door_speed']}{/if}
        <br/>
        {#if current_elevator < 5}Current Elevator Speed is: {thing['elevator_speed']}{/if}
        <br/>
        {#if current_elevator < 5}Current Elevator Speed is: {thing['elevator_speed']}{/if}
        <br/>
        {#if current_elevator >= 5}Current Outdoor Temperature: {thing['outside_temp']}{/if}
        <br/>
        {#if current_elevator >= 5}Current Floor Temp: {thing['elevator_temp']}{/if}
        <br/>
        Days since last service: {thing['usage_time']}
    </div>

</main>

<style>

    #popup {
        position: absolute;
        top: 20vh;
        right: 5vw;
        width: 20vw;
        height: 50vh;
        background-color: white;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
        border-radius: 10px;
        padding: 20px;
        transition: 0.5s;
        opacity: 0;
    }

    @keyframes fadein {
        from { opacity: 0; }
        to   { opacity: 1; }
    }

    .fill {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    main {
        height: 100vh;
        width: 100vw;
        z-index: 1;
        top: 0;
        overflow-x: hidden;
        padding-top: 20px;
        display: flex;
        flex-direction: row;
    }
</style>