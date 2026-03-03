<script lang="ts">
	import MainView from '$lib/components/MainView.svelte';
	import SideBar from '$lib/components/SideBar.svelte';
	import { calendarStepMode } from '$lib/stores/calendar-ui';
</script>

<!-- This is the home page (Calendar View) -->

<main class="mx-auto flex h-full w-[95%] flex-col gap-4 lg:flex-row">
	{#if $calendarStepMode !== 'day'}
		<section class="order-last w-full lg:order-first lg:h-full lg:w-64">
			<SideBar />
		</section>
	{/if}
	<section class="h-full w-full">
		<MainView />
	</section>
</main>
