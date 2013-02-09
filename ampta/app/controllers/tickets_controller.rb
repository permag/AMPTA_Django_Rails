class TicketsController < ApplicationController
  before_filter :sidenav

  def index
    @tickets = Ticket.where(params[:id])
  end

  def show
    @ticket = Ticket.find(params[:id])
  end

  def new
    @ticket = Ticket.new
  end

  def create
    @ticket = Ticket.new(params[:ticket])
    @ticket.user_id = session[:user_id]

    respond_to do |format|
      if @ticket.save
        format.html { redirect_to project_path(@ticket.project), :notice => "Ticket was created." }
      else
        format.html { render :action => "new" }
      end
    end
  end

  def edit
    @ticket = Ticket.find(params[:id])
  end

  def update
    @ticket = Ticket.find(params[:id])
    respond_to do |format|
      if @ticket.update_attributes(params[:ticket])
        format.html { redirect_to project_ticket_path(@ticket.project, @ticket), :notice => "Ticket was updated." }
      else
        format.html { render :action => "edit" }
      end
    end
  end

  def destroy
    @ticket = Ticket.find(params[:id])
    @ticket.destroy

    respond_to do |format|
      format.html { redirect_to project_path(@ticket.project), :notice => 'Ticket was deleted.' }
    end
  end
end
