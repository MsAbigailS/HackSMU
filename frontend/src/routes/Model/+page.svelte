<script lang='ts'>
	import ContextMenu from "$lib/ContextMenu.svelte";
	import ModelPage from "$lib/Model_Page.svelte";
	import type { Context } from "$lib/ContextInterface"
	let context: Context = {name: "nothing"};
	import { focused_elevator } from "$lib/store";
	let current_state = "nothing"

	focused_elevator.subscribe(value => {
		if ($focused_elevator == 0) context = {name: "nothing"};
		if (value < 4) {
			context = {name: `Elevator ${$focused_elevator}`};
		} else {
			context = {name: `HVAC ${$focused_elevator % 4}`};
		}
		// console.log('context is ' + context.name)
	})
</script>

<body>
    <ModelPage/>
	<ContextMenu bind:context />
</body>

<style>
</style>