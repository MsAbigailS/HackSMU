<script>
    import Scene from '$lib/Scene.svelte';
    import { Canvas, extend } from '@threlte/core'
    import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';

    extend({
        OrbitControls
    })

</script>

<main>
    <Canvas>
        <Scene/>
    </Canvas>
</main>

<style>
    main {
        width: 100%;
        height: 100%;
    }
</style>
    