<script lang="ts">
	import { mockEvents, type EventInfo } from '$lib/mockEvents';

	type sideViewEvent = EventInfo;

	let allEvents: sideViewEvent[] = $state(
		mockEvents.map((event) => ({ ...event, toggleClicked: false }))
	);

	let sidebarGroups = [
		{
			title: 'Today',
			events: allEvents
		},
		{
			title: 'Tomorrow',
			events: allEvents
		},
		{
			title: 'This Week',
			events: allEvents
		}
	];
</script>

<aside class="flex h-full w-full flex-col rounded border p-2">
	<h1 class="mb-1 text-base font-semibold">Upcoming Events</h1>
	<div class="scrollbar-hidden min-h-32 flex-1 overflow-y-scroll">
		{#each sidebarGroups as group (group.title)}
			<h1 class="text-md my-2 font-bold outline outline-black">{group.title}</h1>
			{#each group.events as event (event.id)}
				<div class="grid w-full grid-flow-row grid-cols-3 gap-1">
					<div class="event-title col-start-1 col-end-2 text-sm font-bold">
						{event.eventTitle}
						{#if event.food}
							<div class="food-available text-sm font-bold">🍕</div>
						{/if}
					</div>
					<span class="event-time col-3 text-sm font-bold">{event.eventStartTime}</span>
				</div>
				<div class="event-location text-xs">{event.eventLocation}</div>
			{/each}
		{/each}
	</div>
</aside>

<style>
	.scrollbar-hidden::-webkit-scrollbar {
		display: none;
	}
	.scrollbar-hidden {
		-ms-overflow-style: none;
		scrollbar-width: none;
	}
</style>
