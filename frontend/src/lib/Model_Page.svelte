<script lang='ts'>
	import Canvas from "./Canvas.svelte";
    import fetchState from './FetchState';
    import { focused_elevator } from "$lib/store";
    fetchState();

    let current_elevator = 0;
    let popup: HTMLDivElement | null = null;

    focused_elevator.subscribe(value => {
        if (popup == null) return;
        if (value == 0) {
            popup.style.opacity = '0';
            current_elevator = 0;
        } else {
            current_elevator = value;
            popup.style.opacity = '1';
        }

    })

    function updateElevatorValue() {
        focused_elevator.set(current_elevator);
    }

</script>

<main>

    <div class="fill">
        <Canvas/>
    </div>

    <div id="popup" data-theme="light" bind:this={popup} on:on:animationend={() => {updateElevatorValue()}}>
        <hgroup>
            <h3>Elevator {current_elevator}</h3>
            <h3>Condition: Good</h3>
        </hgroup>

        No recommended work yet. 
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