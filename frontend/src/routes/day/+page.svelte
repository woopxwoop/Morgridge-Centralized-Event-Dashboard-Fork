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
		<div class="event-card w-full rounded-xl  p-2 shadow-sm outline outline-black/6 ">
			<button class="event-header flex gap-x-2 bg-white hover:bg-gray-100" type="button" onclick={() => flipArrow(event)}>
				<div class="header-text group">
					<h2 class="event-title title font-bold flex gap-x-3">
						{event.eventTitle}
						<span class="event-location text-sm"> {event.eventLocation}</span>
						<span class="event-time text-sm">@ {event.eventTime}</span>
					</h2>
				</div>
				<span class="arrow {event.arrowUp ? 'rotate' : ''}">v</span>
			</button>

			{#if event.arrowUp}
				<div class="event-details">
					<h1 class="flex gap-x-1">
						<p class="host">{event.eventHost}</p>
						<img class="" src = "" alt = ""/> <!--Host logo-->
					</h1>
					<h2 class="flex gap-x-2">
						<p class="description">{event.eventDescription}</p>
						<img class="" src = "" alt = ""/> <!--Event image-->
					</h2>
				</div>
			{/if}
		</div>
	{/each}
</div>

<style>
	.rotate {
		transform: rotate(180deg);
	}
</style>
