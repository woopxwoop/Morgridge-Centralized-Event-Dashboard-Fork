<!-- This is the page for a specific day -->
<script lang="ts">
	let { data }: { data: { selectedDate: string | null } } = $props();

	interface EventInfo {
		id: number;
		eventTitle: string;
		eventHost: string;
		eventLocation: string;
		eventTime: string;
		eventDescription: string;
		pizza: boolean;
		arrowUp: boolean; //arrowUp-open !arrowUp-closed
	}

	let dayEvents: EventInfo[] = $state([
		{
			id: 1,
			eventTitle: 'Craft Night Social',
			eventHost: 'Girls Who Code-Madison Chapter',
			eventLocation: 'Morgridge Hall Student Org Lounge (2nd floor)',
			eventTime: '7:30 - 8:30 PM',
			eventDescription:
				'Join us for a break from studying to decorate our club locker and meet other fellow members! We will have pizza 🍕 and arts/craft supplies 🖌️✂️ for you to make decorations. We hope to see you there!!',
			pizza: true,
			arrowUp: false
		},
		{
			id: 2,
			eventTitle: 'WebTalks',
			eventHost: 'Weblabs',
			eventLocation: 'Morgridge Hall Rm. 2556',
			eventTime: '6:00pm - 7:00pm',
			eventDescription:
				"WebLabs is hosting a workshop with a frontend engineer from Fetch on publishing a website using SvelteKit and GitHub Actions. Whether you're a frontend warrior or just interested in standing up a portfolio site for your resume, this workshop will have something for everyone! Like usual for WebLabs, this event will feature pizza 🍕",
			pizza: true,
			arrowUp: false
		}
	]);

	function flipArrow(clickEvent: EventInfo): void {
		clickEvent.arrowUp = !clickEvent.arrowUp;
	}
</script>

{#if data.selectedDate}
	<p>Showing events for: {data.selectedDate}</p>
{:else}
	<p>No date selected. Go back to calendar and choose a day.</p>
{/if}

<div class="schedule-container">
	{#each dayEvents as event (event.id)}
		<div class="event-card">
			<button class="event-header" type="button" onclick={() => flipArrow(event)}>
				<div class="header-text">
					<h2 class="title">{event.eventTitle} {event.eventLocation} {event.eventTime}</h2>
					<p class="time"></p>
				</div>
				<span class="arrow {event.arrowUp ? 'rotate' : ''}">v</span>
			</button>

			{#if event.arrowUp}
				<div class="event-details">
					<p class="host">{event.eventHost}</p>
					<p class="description">{event.eventDescription}</p>
				</div>
			{/if}
		</div>
	{/each}
</div>

<style>
	.event-header {
		gap: 10px;
		display: flex;
	}

	span {
		transition: 0.1s;
		display: inline-block;
	}

	.rotate {
		transform: rotate(180deg);
	}
</style>
