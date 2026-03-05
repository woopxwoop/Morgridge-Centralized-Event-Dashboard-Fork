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

<aside class="flex h-full w-full flex-col rounded border p-4 hover:overflow-y-auto">
	<h2 class="mb-2 text-base font-semibold">Upcoming Events</h2>
	<div class="min-h-32 flex-1 text-sm">
		{#each sidebarGroups as group}
			<h3 class="font-bold">{group.title}</h3>
			{#each group.events as event (event.id)}
				<div class="event-card w-full rounded p-2 shadow-sm outline outline-black/6">
					<h2 class="event-title title flex font-bold">
						{event.eventTitle}
						{#if event.food}
							<span class="food-available">🍕</span>
						{/if}
						<span class="event-location text-sm"> {event.eventLocation}</span>
						<span class="event-time text-sm">@ {event.eventStartTime}</span>
					</h2>
				</div>
			{/each}
		{/each}
	</div>
</aside>
