<script lang="ts">
	import { mockEvents, type EventInfo } from '$lib/mockEvents';
	import chevron from '$lib/assets/up-chevron.svg';

	type DayViewEvent = EventInfo & { toggleClicked: boolean };

	let dayEvents: DayViewEvent[] = $state(
		mockEvents.map(event => ({...event, toggleClicked: false}))
	);

	let { selectedDate = null }: { selectedDate: string | null } = $props();

	function viewDetails(eventId: number) {
		const event = dayEvents.find(e => e.id === eventId);
		if (event) {
			event.toggleClicked = !event.toggleClicked;
		}
	}
</script>

{#if selectedDate}
	<p>Showing events for: {selectedDate}</p>
{:else}
	<p>No date selected. Go back to calendar and choose a day.</p>
{/if}

<div class="dayEvent-container">
	{#each dayEvents as event (event.id)}
		<div class="event-card w-full rounded-xl p-2 shadow-sm outline outline-black/6">
			<button
				class="event-header flex h-full w-full gap-x-2 bg-white rounded-xl hover:bg-gray-100"
				type="button"
				onclick={() => viewDetails(event.id)}
			>
				<div class="header-text group">
					<h2 class="event-title title flex font-bold">
						{event.eventTitle}
						{#if event.food}
							<span class="food-available">🍕</span>
						{/if}
						<span class="event-location text-sm"> {event.eventLocation}</span>
						<span class="event-time text-sm">@ {event.eventStartTime}</span>
					</h2>
				</div>
				<span class="toggle w-6 h-6"> <img class="{event.toggleClicked ? '' : 'rotate-180'}" src={chevron} alt="toggle" /></span>
			</button>

			{#if event.toggleClicked}
				<div class="event-details">
					<h1 class="flex gap-x-1">
						<p class="host">{event.eventHost}</p>
						<img class="" src="" alt="" />
					</h1>
					<h2 class="flex gap-x-2">
						<p class="description">{event.eventDescription}</p>
						<img class="" src="" alt="" />
					</h2>
				</div>
			{/if}
		</div>
	{/each}
</div>
