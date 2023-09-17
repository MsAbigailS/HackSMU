<script>
    import Scene from '$lib/Scene.svelte';
    import { Canvas, extend } from '@threlte/core'
    import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';

    extend({
        OrbitControls
    })

</script>

<div style = "height:50vh">
    <Canvas>
        <Scene/>
    </Canvas>
</div>
    