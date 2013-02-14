class TicketsController < ApplicationController
  before_filter :confirm_user_new, :only => [:new, :create, :show]
  before_filter :confirm_user_edit, :only => [:edit, :update, :destroy]
  before_filter :confirm_user_index, :only => [:index]
  before_filter :sidenav

  def index
    # if url: /tickets/ -show all tickets for user. if url: /project/id/tickets/ -show all tickets for project
    if params[:project_id]
      @project_name = Project.find(params[:project_id]).name
      @tickets = Ticket.where("project_id = ?", params[:project_id])
    else
      @tickets = Ticket.where("user_id = ?", user_logged_in)
    end
  end

  def show
    @ticket = Ticket.find(params[:id])

    # is ticket or project owner
    if @ticket.user_id == user_logged_in || @ticket.project.owner_id == user_logged_in
      @owner_menu = true
    end
  end

  def new
    @ticket = Ticket.new
  end

  def create
    @ticket = Ticket.new(params[:ticket])
    @ticket.user_id = user_logged_in

    respond_to do |format|
      if @ticket.save
        format.html { redirect_to project_path(@ticket.project), :notice => "Ticket \"#{@ticket.name}\" was created." }
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
        format.html { redirect_to project_ticket_path(@ticket.project, @ticket), :notice => "Ticket \"#{@ticket.name}\" was updated." }
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

  ##
  # check to see if user is ticket owner or project owner
  #
  def confirm_user_edit
    ticket =  Ticket.find(params[:id])
    unless ticket.user_id == user_logged_in || ticket.project.owner_id == user_logged_in
      flash[:notice] = "You don't have the permission to do that."
      redirect_to home_error_path
      return false
    else
      return true
    end
  end

  def confirm_user_new
    project = Project.find(params[:project_id]) 
    unless project.owner_id == user_logged_in || project.users.exists?(user_logged_in)
      flash[:notice] = "You don't have the permission to do that."
      redirect_to home_error_path
      return false
    else
      return true
    end
  end

  def confirm_user_index
    if params[:project_id] && !Project.find(params[:project_id]).users.exists?(user_logged_in)
      flash[:notice] = "You don't have the permission to do that."
      redirect_to home_error_path
      return false
    else
      return true
    end
  end

end
