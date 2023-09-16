<script>
    import { OrbitControls } from '@threlte/extras'
    import { T } from '@threlte/core'
  </script>
  <T.PerspectiveCamera
    makeDefault
    position={[5, 8, 5]}
  >
    <OrbitControls
      on:change={(e) => {
        console.log(e)
      }}
    />
  </T.PerspectiveCamera>