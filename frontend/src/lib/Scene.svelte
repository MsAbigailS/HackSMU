<script lang="ts">
    import { T } from '@threlte/core'
    import { Grid, interactivity } from '@threlte/extras'
    import { spring } from 'svelte/motion'
    import Camera from './Camera.svelte'
    import Model from './Model.svelte';
    import HvacModel from './HVAC_Model.svelte';

    interactivity();

    const scale = spring(1);

  </script>
  <Camera />
  <T.DirectionalLight position={[1, 2, 5]} />
  <Model/>
  <HvacModel elevator_id={5}/>
  <HvacModel y_offset={3} elevator_id={6}/>
  <HvacModel y_offset={6} elevator_id={7}/>
  <Grid
    position.y={-0.001}
    cellColor="#ffffff"
    sectionColor="#ffffff"
    sectionThickness={0}
    fadeDistance={25}
    cellSize={2}
  />