<script>
	import Canvas from "./Canvas.svelte";

</script>

<div class="">

    <div class="split left">
        <Canvas/>
    </div>

    <div class ="split right">
        <div>
            <input/>
        </div>
        <div class="eventBox">
            hi
        </div>
    </div>

</div>

<style>
    .split {
        height: 100%;
        width: 50%;
        position: fixed;
        z-index: 1;
        top: 0;
        overflow-x: hidden;
        padding-top: 20px;
    }
    .left {
        left: 0;
    }
    .right {
        right: 0;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .eventBox {
        height: 40vh;
        width: 40vw;
        max-height: 600px;
        max-width: 400px;
        background-color: blue;
    }
</style>