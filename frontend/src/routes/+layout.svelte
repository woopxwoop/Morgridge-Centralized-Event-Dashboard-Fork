<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';
	import TopBar from '$lib/components/TopBar.svelte';

	let { children } = $props();
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>

<div class="flex w-full flex-col gap-8 pb-8 lg:h-screen">
	<div class="flex-none">
		<TopBar />
	</div>
	<div class="min-h-0 flex-1">
		{@render children()}
	</div>
</div>
