<script lang="ts">
	import { mockEvents, type EventInfo } from '$lib/mockEvents';

	type sideViewEvent = EventInfo;

	let allEvents: sideViewEvent[] = $state(
		mockEvents.map(event => ({...event, toggleClicked: false}))
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
	]
</script>

<aside class="flex h-full w-full flex-col rounded border p-2">
	<h1 class="mb-1 text-base font-semibold">Upcoming Events</h1>
	<div class="min-h-32 flex-1 overflow-y-scroll scrollbar-hidden">
		{#each sidebarGroups as group}
			<h1 class="font-bold text-md my-2 outline outline-black/100">{group.title}</h1>
			{#each group.events as event (event.id)}
				<div class="w-full flex grid grid-flow-row grid-cols-3 gap-1">
					<div class="event-title text-sm font-bold col-start-1 col-end-2">{event.eventTitle}
					{#if event.food}
						<div class="food-available text-sm font-bold">🍕</div>
					{/if}
					</div>
					<span class="event-time text-sm font-bold col-3">{event.eventStartTime}</span>
				</div>
				<div class="event-location text-xs"> {event.eventLocation}</div>
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