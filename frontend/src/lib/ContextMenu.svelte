<!-- 
Inspired from: Context Menu https://svelte.dev/repl/3a33725c3adb4f57b46b597f9dade0c1?version=3.25.0
-->

<script lang='ts'>
	import Phone from '$lib/icons/Phone.svelte'
	import Graph from '$lib/icons/Graph.svelte';
    let pos = { x: 0, y: 0 }
    let menu = { h: 200, w: 170 }
    let browser = { h: 0, w: 0 }
    let showMenu = false;

    function rightClickContextMenu(e: { clientX: any; clientY: any; }){
        showMenu = true
        browser = {
            w: window.innerWidth,
            h: window.innerHeight
        };
        pos = {
            x: e.clientX,
            y: e.clientY + menu.h / 2
        };
        // If bottom part of context menu will be displayed
        // after right-click, then change the position of the
        // context menu. This position is controlled by `top` and `left`
        // at inline style. 
        // Instead of context menu is displayed from top left of cursor position
        // when right-click occur, it will be displayed from bottom left.
        if (browser.h -  pos.y < menu.h)
            pos.y = pos.y - menu.h
        if (browser.w -  pos.x < menu.w)
            pos.x = pos.x - menu.w
    }
    function onPageClick(e: any){
        // To make context menu disappear when
        // mouse is clicked outside context menu
        showMenu = false;
    }
    function getContextMenuDimension(node: HTMLElement){
        // This function will get context menu dimension
        // when navigation is shown => showMenu = true
        let height = node.offsetHeight
        let width = node.offsetWidth
        menu = {
            h: height,
            w: width
        }
    }
    function msgTechnician(){
		console.log('add item');
    }

</script>
<svelte:head>
    <!-- You can change icon sets according to your taste. Change `class` value in `menuItems` above to represent your icons. -->
    <!-- <link rel="stylesheet" href="/icon/css/mfglabs_iconset.css"> -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</svelte:head>
<style>
    .navbar{
        display: inline-flex;
        border: 1px #999 solid;
        width: 170px;
		height: 200px;
		padding-top: 10px;
		padding-bottom: 10px;
        background-color: #fff;
        border-radius: 10px;
        overflow: hidden;
        flex-direction: column;
    }

	button {
		color: black;
		border: none;
		background-color: white;
		text-align: center;
		text-decoration: none;
		font-size: 16px;
		padding: 0;
		transition: 0.1s;
		margin-bottom: 0;
		margin-top: 0;
		border-radius: 10px;
		display: flex;
		flex-direction: row;
		justify-content: space-evenly;
	}

	button:hover {
		background-color: whitesmoke;
	}
</style>

{#if showMenu}
<nav use:getContextMenuDimension style="position: absolute; top:{pos.y}px; left:{pos.x}px">
    <div class="navbar" id="navbar">
		<button on:click={msgTechnician}>Notify Technician<Phone/></button>
		<button>View Diagnostics<Graph/></button>
    </div>
</nav>
{/if}

<svelte:window on:contextmenu|preventDefault={rightClickContextMenu} 
on:click={onPageClick} />

